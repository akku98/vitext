from googletrans import Translator , constants
from pprint import pprint

translator=Translator()
translation=translator.translate("Hello", src='en',dest='hi')
print(f"{translation.origin} ({translation.src})--> {translation.text} ({translation.dest})")
