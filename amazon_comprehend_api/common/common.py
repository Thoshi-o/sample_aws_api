import boto3
import json

class comprehender():
    comprehend_instance = ""
    input_text = ""
    def __init__(self, input_text):
        print("init")
        self.input_text = input_text
        self.comprehend_instance = boto3.client(service_name='comprehend', region_name='ap-northeast-1')
    
    def detect_language(self):
        print('Calling DetectDominantLanguage')
        print(json.dumps(self.comprehend_instance.detect_dominant_language(Text = self.input_text), sort_keys=True, indent=4))
        print("End of DetectDominantLanguage\n")

    def analyze_syntax(self):
        print('Calling DetectSyntax')
        print(json.dumps(self.comprehend_instance.detect_syntax(Text=self.input_text, LanguageCode='en'), sort_keys=True, indent=4))
        print('End of DetectSyntax\n')
    
    def detect_key_phrase(self):
        print('Calling DetectKeyPhrases')
        print(json.dumps(self.comprehend_instance.detect_key_phrases(Text=self.input_text, LanguageCode='en'), sort_keys=True, indent=4))
        print('End of DetectKeyPhrases\n')
    
    def detect_name_entity(self):
        print('Calling DetectEntities')
        print(json.dumps(self.comprehend_instance.detect_entities(Text=self.input_text, LanguageCode='ja'), sort_keys=True, indent=4))
        print('End of DetectEntities\n')

    def detect_sentiment(self):
        print('Calling DetectSentiment')
        print(json.dumps(self.comprehend_instance.detect_sentiment(Text=self.input_text, LanguageCode='ja'), sort_keys=True, indent=4))
        print('End of DetectSentiment\n')


comprehender("眠い").detect_language()