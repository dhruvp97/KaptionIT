# KaptionIT 

An artificial intelligence with Vision to caption and extract meaning behind images. To learn more about the project check out our devpost, https://devpost.com/software/mhl_1.

## Inspiration

Suppose someone posts a picture on social media without a caption, there are multiple different interpretations of that picture through everyone’s minds and so the picture loses its actual meaning. Instead, having a caption would allow the poster and viewer to get a clear meaning of the picture (an effective way of communicating your emotions/meaning).

## What it does? 

In simple terms, provided an image, it generates a caption. We start off by allowing the user to upload any image of their choice, and feed it to the **Google Cloud's Vision API** to generate meaningful labels. Using the labels and salience score, the algorithm searches the internet for content that relates to the image. The content is then processed by **Google Cloud's Natural Language API** to produce best matching entities related to the meaning of the text. Lastly, with the use of a heuristic function we match the appropriate caption to the image.

## Next Steps

Nowadays, the use of smartphones is very high. Although we have made an application for Windows, we would like to further develop the accessibility of our software for all types of smartphone users. It would make perfect sense to have such captioning software for mobiles since the majority of people use social media on their smartphones.
