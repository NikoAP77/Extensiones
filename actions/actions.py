from typing import Dict, Text, Any, List, Union, Optional
from rasa_core_sdk.forms import FormAction
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from .connection_postgresql import DataUpdate
"""class ActionNombre (Action):
    def name(self) -> Text:
        #Identificador unico del formulario
        return "action_nombre"

    def run (self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_nombre")
        return [SlotSet('nombre', tracker.latest_message['text'])]

class ActionApellido (Action):
    def name(self)-> Text:
        # Identificador unico del formulario
        return "action_apellido"

    def run (self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_apellido")
        return [SlotSet('apellido', tracker.latest_message['text'])]

class ActionComentario (Action):
    def name(self)-> Text:
        # Identificador unico del formulario
        return "action_comentario"

    def run (self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_comentario")
        return [SlotSet('comentario', tracker.latest_message['text'])]"""

class ActionGuardarDB (Action):
    def name(self)-> Text:
        # Identificador unico del formulario
        return "validate_action_guardar"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        print("Tracker ",tracker)
        DataUpdate(tracker.get_slot("nombre"),
                   tracker.get_slot("apellido"),
                   tracker.get_slot("comentario"))
        dispatcher.utter_message("Gracias por guardar su informacion...")
        return [SlotSet('nombre', None), SlotSet('apellido', None),SlotSet('comentario', None)]

"""class MenuNumbers(Action):

    def name(self) -> Text:
        print("Entro")
        return "action_menu_uno"

    def run (self, dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        ultimo = tracker.latest_message['intent'].get('name')
        msm_obtenido = (tracker.latest_message)['text'].lower()
        print("ut", ultimo)
        print("Este mensaje ingreso el usuario: ", msm_obtenido)
        slot_value = tracker.get_slot(ultimo)
        if msm_obtenido == "1":
            dispatcher.utter_message(template="utter_Pa1dos")
        elif msm_obtenido == "2":
            dispatcher.utter_message(template="utter_servicios")
            
        elif msm_obtenido == "3":
            dispatcher.utter_message(template="utter_cotizacion")
        else:
            dispatcher.utter_message(template="utter_incorrecta")
            print("No selecciono ninguna opcion")
        return []

    def start_story_events(self, story_intent):
        # type: (Text) -> List[Dict]
        return self.deactivate() + [ActionExecuted("action_listen")] + [UserUttered("/" + story_intent, {
            "intent": {"name": story_intent, "confidence": 1.0},
            "entities": {}
        })]"""

class MenuNumbersDos (Action):
    def name(self) -> Text:
        print("Entro menu dosssss")
        return "action_menu_dos"

    def run (self, dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any])-> List[Dict[Text, Any]]:
        digito = tracker.latest_message['intent'].get('name')
        msm_obtenido = (tracker.latest_message)['text'].lower()
        print("ut", digito)
        print("Este mensaje ingreso el usuario menu dos: ", obtenido)
        slot_value = tracker.get_slot(digito)
        if msm_obtenido == "1":
            dispatcher.utter_message(template="utter_software")
        elif msm_obtenido == "2":
            dispatcher.utter_message(template="utter_domotica")
        elif msm_obtenido == "3":
            dispatcher.utter_message(template="utter_comunicacion")
        elif msm_obtenido == "4":
            dispatcher.utter_message(template="utter_contabilidad")
        elif msm_obtenido == "5":
            dispatcher.utter_message(template="utter_marketing")
        else:
            dispatcher.utter_message(template="")
            print("No selecciono ninguna opcion")
        return []






