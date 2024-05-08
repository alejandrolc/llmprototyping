from typing import List
import inspect
import ollama
from .llm_interface import LLMChatCompletion, LLMChatCompletionFactory, Message, Response
from .error import LLMException

class LLMOLlamaChatCompletion(LLMChatCompletion):
    def __init__(self, host, model_name, model_details):
        self.model_name = model_name
        self.model_details = model_details
        self._client = ollama.Client(host=host)

    @property
    def context_size(self):
        raise NotImplemented()

    def query(self, messages:List[Message], json_response=False, temperature=1.0):
        if not isinstance(temperature,float) and not isinstance(temperature,int):
            raise LLMException.param_error("temperature must be a float")

        try:
            rformat = 'json' if json_response else ''
            r = self._client.chat(
                messages = [m.to_dict() for m in messages],
                model = self.model_details['name'],
                options = {'temperature': temperature},
                format = rformat,
            )
            rcontent = r['message']['content']
            rrole = r['message']['role']
            msg = Message(content=rcontent, role=rrole)
            input_tokens = r['prompt_eval_count']
            output_tokens = r['eval_count']
            response = Response(message=msg, input_token_count=input_tokens, output_token_count=output_tokens)
        except ollama.ResponseError as e:
            response = Response.error_response(status_code = e.status_code, error = e.error)
        except Exception as e:
            response = Response.error_response(status_code = "exception", error = e)

        return response

    @classmethod
    def from_dict(cls, data):
        return cls(model_name=cls.cls_model_name, host=cls.cls_host, model_details = cls.cls_model_details)

_class_counter = 1
def discover(host):
    global _class_counter

    client = ollama.Client(host=host)
    for model in client.list()['models']:
        model_name = f'ollama/{model["name"]}'
        if LLMChatCompletionFactory.model_registered(model_name):
            continue

        attrs = {
            'cls_model_name': model_name,
            'cls_model_details': model,
            'cls_host': host
        }
        class_name = f'ollama_model_{_class_counter}'
        _class_counter += 1
        model_class = type(class_name, (LLMOLlamaChatCompletion,), attrs)
        LLMChatCompletionFactory.register(name=model_name, class_obj=model_class)

def pull_model(host, model_name):
    try:
        client = ollama.Client(host=host)
        resp = client.pull(model_name)
        if resp.get('status') == 'success':
            discover(host)
            return True
    except:
        return False


def init():
    pass
