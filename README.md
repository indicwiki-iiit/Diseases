# Diseases-Tewiki

This repository contains all the work that was done as a part of enriching Tewiki Hindi wikipedia in the Diseases and Conditions domain.

## Stages of the project

The following ordered list will give an idea as to what stage the project currently is in:

- [x] Scrape Data from Web sources
- [x] Clean and Format the data
- [x] Scrape image URLs from Wiki commons
- [x] Scrape infobox information from Wikipedia
- [x] Create a sample article
- [x] Review of the sample article
- [x] Work on feedback from review of sample article
- [x] Review of the dataset
- [x] Create template for article generation
- [x] Review of the template
- [x] Work on feedback from review of template
- [x] Create the XML dump for all the diseases to be published

## Folders

- `Datasets`: Contains all the dataset (csv) files that have been used for this project.
- `Code`: Contains all the code that has been used in the project.
- `Template`: Contains the jinja template for the XML generation of a Disease article.

### Datasets

This folder contains the final dataset as well as some other dataset that have been used in the project:

- [FinalDiseasesHindi](./Datasets/FinalDiseasesHindi.csv): this file contains the final dataset that will be used for article generation. This file contains data on 1157 diseases and has 24 attributes. Its excel version is [here](./Datasets/FinalDiseasesHindi.xlsx).
- [Others/ScrapedEnglish](./Datasets/Others/ScrapedEnglish.csv): contains the original scraped data on diseases and conditions from Mayo Clinic and NHS.
- [Others/InfoboxEnglish](./Datasets/Others/InfoboxEnglish.csv): contains the infobox attributes that were scraped from the diseases' English wikipedia pages.
- [Others/MergedEnglish](./Datasets/Others/MergedEnglish.csv): contains the merged dataset file of the original scraped data and the infobox data. Its excel version can be found [here](./Datasets/Others/MergedEnglish.xlsx).

### Code

This folder contains various files:

- [scrape](./Code/scrape.ipynb): it contains the code for scraping the NHS website links available for the diseases. These links can then be used to scrape the information for some diseases which Mayo Clinic had little to no information on. It also has code for generating a sweet viz report on the dataset
- [format](./Code/format.ipynb): it contains the code for formatting the original unstructured dataset into a more structured form. Helps to remove sentences from attributes that are too informal, casual, and directional. Moreover, it also removes the sentences which are part of the website and does not offer any information regarding the disease.
- [check](./Code/check.ipynb): it contains the code for checking which rows of the dataset are valid to be included in the final dataset. Highlights the diseases for which very little information is present and an article cannot be generated on them. Helped to reduce the number from 1183 possible articles to 1157 articles.
- [images](./Code/images.ipynb): it contains the code for scraping images of diseases from Wiki commons. The image is essentially used in the English wikipedia page of the disease.
- [infobox](./Code/infobox.ipynb): it contains the code for scraping infobox data available on the English wikipedia pages of the diseases. Therefore, our infobox will follow the same template as followed by diseases on wikipedia.
- [translate](./Code/translate.ipynb): it contains the code for using Google translator to translate English scraped dataset into Hindi dataset. It also contains code for transliteration.
- [translateInfobox](./Code/translateInfobox.ipynb): this file contains the code for translating the scraped English infobox information.
- [merge](./Code/merge.ipynb): this file contains the code for merging the translated files of the website scraped data and infobox data.

### Generating articles

- [template](./Template/template.j2): it contains the template for the structure of a disease and condition article
- [genXML](./genXML.py): it contains the backbone structure for conversion to XML
- [render](./render.py): it contains the code for generating XML dump of articles using the template and the dataset
- [diseases](./diseases.xml): the final XML dump file of all the 1157 diseases and conditions
