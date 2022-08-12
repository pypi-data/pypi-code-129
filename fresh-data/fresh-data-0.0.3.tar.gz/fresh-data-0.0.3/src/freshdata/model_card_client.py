import requests

class ModelCardClient():
    def __init__(
        self, 
        id:str=None, # what you have from the server
        model_card:dict={},
        api_key:str=None,
        endpoint:str='http://freshdata.ai'
    ):
        if api_key is None:
            raise TypeError("api_key is required, please visit http://www.freshdata.ai/ to set up an account")

        if endpoint is None:
            raise TypeError("endpoint is required")

        self.api_key = api_key
        self.endpoint = endpoint
        self.model_card = model_card

        # dealing with id
        found_id = None
        if (id is None) and (model_card.get('id', None) is not None):
            found_id = model_card['id']
        elif id is not None:
            found_id = id

            if self.model_card is None:
                self.model_card = self._load_model_card(found_id)

        if found_id is None:
            self.id = self.create_new_model_card_id()
        else:
            self.id = found_id
        self.model_card['id'] = found_id
    
    def create_new_model_card_id(self):
        url = self.endpoint + '/new_model_card_id'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        id = response.json()['id']
        return id
    
    def load(self, id:str):
        # loads a model card from the server
        self.id = id
        self.model_card = self._load_model_card(id)


    def _load_model_card(self, id:str):
        # loads a model card from the server
        url = self.endpoint + '/load'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {'id': id}
        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        model_card = response.json()['model_card']
        return model_card

    def _save(self, fname:str='model_card_rendered.html', just_locally:bool=False):
        # saves a rendered model card to file

        with open(fname, 'w') as f:
            f.write(self.model_card)

        if not just_locally:
            url = self.endpoint + '/save'
            headers = {'Authorization': f'Bearer {self.api_key}'}
            data = {'model_card': self.model_card, "id": self.id}
            response = requests.post(url, headers=headers, json=data)

            if response.status_code != 200:
                raise Exception(f"Error: {response.status_code}")
    
    def render(
        self, 
        display:bool=True, 
        save:bool=True, 
        fname:str='model_card_rendered.html'
    ):
        # check if inside a jupyter notebook
        try:
            from IPython import get_ipython
            ipython = get_ipython()
            if ipython is not None:
                display = False
        except Exception as e:
            pass
        
        if save:
            if fname is None:
                raise Exception("fname is required")
        
        # get rendered model card from server
        url = self.endpoint + '/render'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {'model_card': self.model_card}
        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        rendered = response.json()['rendered']
            
        if save:
            self._save(fname,just_locally=False)
        if display:
            return display(HTML(rendered))
        
        return rendered
