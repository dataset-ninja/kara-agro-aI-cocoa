from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "KaraAgro AI Cocoa"
PROJECT_NAME_FULL: str = "The KaraAgroAI Cocoa Dataset"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC0_1_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Agricultural()]
CATEGORY: Category = Category.Agriculture()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2022-07-29"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = (
    "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BBGQSP"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 12700427
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/kara-agro-aI-cocoa"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BBGQSP#"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "anthracnose-leaf": [230, 25, 75],
    "anthracnose pod": [60, 180, 75],
    "cocoa-swollen-shoot-virus-leaf": [255, 225, 25],
    "cocoa-swollen-shoot-virus-pod": [0, 130, 200],
    "cocoa-swollen-shoot-virus-stem": [245, 130, 48],
    "healthy-cocoa": [145, 30, 180],
    "healthy-cocoa-leaf": [70, 240, 240],
    "healthy-cocoa-pod": [240, 50, 230],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[
    Union[str, List[str], Dict[str, str]]
] = "https://dataverse.harvard.edu/file.xhtml?fileId=6419433&version=6.1"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Akogo Darlington",
    "Nakatumba-Nabende Joyce",
    "Christabel Acquaye",
    "Emmanuel Amoako",
    "Jerry Buaba",
    "Issah Samori",
    "Tusubira Francis Jeremy",
    "Namanya Gloria",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["support@dataverse.harvard.edu"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "University of Ghana"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.ug.edu.gh/"

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "__PRETEXT__": "Additionally, every image have information about its parent folder: ***anthracnose_01-anthracnose_04***, ***cssvd_01-cssvd_04***, ***healthy_01-healthy_05***"
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
