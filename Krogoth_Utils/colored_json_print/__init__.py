# Matt Andrzejczuk (c) 2018
# MIT License

from Krogoth_Utils.pyink import ink
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
import json


class PrettyPrint():
    @classmethod
    def full_format(cls, jsonstr):
        try:
            json_object: json = json.loads(str(jsonstr))
            json_str: str = json.dumps(json_object, sort_keys=True, indent=2)
            ink.print_green("\n",
                            highlight(json_str, JsonLexer(), TerminalFormatter())
                            )
        except Exception as e:
            ink.print_red("\n\nPrettyPrint Has Failed: ", str(e))
    
    @classmethod
    def single_line(cls, jsonstr):
        try:
            json_object: json = json.loads(str(jsonstr))
            json_str: str = json.dumps(json_object, sort_keys=True)
            ink.print_green("\n",
                            highlight(json_str, JsonLexer(), TerminalFormatter())
                            )
        except Exception as e:
            ink.print_red("\n\nsingle_line Has Failed: ", str(e))
