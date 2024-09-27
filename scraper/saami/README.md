# Scrape SAAMI specs

## API key
You need an openai api key. Then set it as an environment variable to be picked up. For example:
`export OPENAI_API_KEY=key_here`

## Dependencies
To run this scraper first install the required libraries via:
`pip install -r requirements`

## Running
`python3 scrape.py`

The current version will do the following:
* It'll download the main cartridge pdf from the SAAMI website
* The file is split into one pdf file per cartridge
* These files are sent individually to the openai api to be parsed
* The returned json is not perfect, so we massage it a bit
  
This should give you a json file for each cartridge.
These files can then be merged into one saami.json file.

It is possible to resume the process if it fails in the middle. Any existing json files will simply be skipped.

# TODOs
Use the new structured output feature.
https://openai.com/index/introducing-structured-outputs-in-the-api/