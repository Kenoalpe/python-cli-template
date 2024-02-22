import inquirer
import logging.config

logging.getLogger(__name__)


class MenuView:

    @staticmethod
    def display(message: str, choices: list):
        """
        show the inquirer list prompt and return the answer.
        """
        questions = [
            inquirer.List(
                'action',
                message=message,
                choices=choices,
            )
        ]
        try:
            return inquirer.prompt(questions)['action']
        except TypeError:
            logging.error("Object for the questions prompt is incorrect!")
            return None
