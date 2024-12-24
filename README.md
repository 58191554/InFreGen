# InFreGen
A Group Work of ![Microsoft Fabric and AI Learning Hackathon](https://microsoftfabric.devpost.com/)
See our [WebPage]() for more details.

## Pipeline
- User Input Parser: `userInputParser.ipynb` get taskID
- GPT4o Talker: `GPT4otalker.ipynb` get keywords from the user input
- URL Fetcher: `urlFetch.ipynb` get image urls by the keywords
- Image Fetcher: `imageFetcher.ipynb` download the images and save to the lakehouse
- Object Detector: `GroundingDINO_with_Segment_Anything.ipynb` get the object detection results
    - Detect objects in images based on text prompts
    - Generate segmentation masks for the detected objects
    - Process and crop images based on the detections
    - Use the clip to get the image description
    - Use SAM to generate the segmentation masks
- Resizer: `Resize.ipynb` resize the images, update the pic table
- Packer: `Packing.ipynb` pack the images into a single image, update the pic table
- Email Sender: get the pic package and send to the user with fabric pipeline
## Data Definition
- Metadata: `MetaTableNotebook.ipynb` define the metadata of the images
    - `pic`: store the image urls, descriptions, and other information
    - `task`: store the task information

- Database: `sqlite_db.py` define the database of the task and the pic
    - `task`: store the task information
    - `pic`: store the image urls, descriptions, and other information
to check the database, run `sqlite3 tasks.db`
```sql
SELECT * FROM tasks;
```
to end the database viewer, run `.exit`
