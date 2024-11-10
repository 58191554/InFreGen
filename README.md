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
- Resizer: `Resize.ipynb` resize the images, update the pic table
- Packer: `Packing.ipynb` pack the images into a single image, update the pic table
- Email Sender: get the pic package and send to the user with fabric pipeline
