from __future__ import print_function, unicode_literals
import sys

from unicodedata import category

class Utils():

    def __init__(self):

        pass

    def print_version(self):
        version_file = open("version.txt", "r")
        version = version_file.read()
        version_file.close()
        return(version)


    def present_checkbox(self, category_list_for_checkbox, list_type="category"):
        from whaaaaat import Separator, Token, print_json, prompt, style_from_dict

        style = style_from_dict(
            {
                Token.Separator: "#F1C40F",
                Token.QuestionMark: "#FF9D00 bold",
                Token.Selected: "#229954",
                Token.Pointer: "#FF0E0E bold",
                Token.Instruction: "#229954",
                Token.Answer: "#5F819D bold",
                Token.Question: "",
            }
        )


        checkbox_content = [
            {
                'type': 'checkbox',
                'message': 'Select %s' % list_type,
                'name': list_type,
                'choices': category_list_for_checkbox,
                'validate': lambda answer: 'You must choose at least one %s.' % list_type \
                    if len(answer) == 0 else True
            }
        ]

        answers = prompt(checkbox_content , style=style)
        return(answers)

    def exit_error(self, error_message):

        """ Exit with message """

        sys.exit("‼️  Error: %s" % error_message)

    def get_gcp_secret(self, project_id, secret_id):

        """ Get secret from GCP """

        # Import the Secret Manager client library.
        from google.cloud import secretmanager
        import google_crc32c

        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()

        # Build the resource name of the secret version.
        name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"

        # Access the secret version.
        response = client.access_secret_version(request={"name": name})

        # Verify payload checksum.
        crc32c = google_crc32c.Checksum()
        crc32c.update(response.payload.data)
        if response.payload.data_crc32c != int(crc32c.hexdigest(), 16):
            print("Data corruption detected.")
            return response

        payload = response.payload.data.decode("UTF-8")
        return("{}".format(payload))