from dash import *
import dash_image_gallery


app = Dash(__name__)

app.layout = html.Div([
    dash_image_gallery.DashImageGallery(
        id='input',
        items=[
            {
                "original": "/assets/image1.png",
                "thumbnail": "/assets/image1.png",
            },
            {
                "original": "/assets/image2.png",
                "thumbnail": "/assets/image2.png",
            },
            {
                "original": "/assets/image3.png",
                "thumbnail": "/assets/image3.png",
            },
            {
                "original": "/assets/image4.png",
                "thumbnail": "/assets/image4.png",
            },
        ],
        infinite=True,
        lazyLoad=False,
        showNav=True,
        showThumbnails=True,
        thumbnailPosition='bottom',
        showFullscreenButton=True,
        useBrowserFullscreen=True,
        useTranslate3D=True,
        showPlayButton=True,
        isRTL=False,
        showBullets=False,
        showIndex=True,
        autoPlay=True,
        disableThumbnailScroll=False,
        disableKeyDown=False,
        disableSwipe=False,
        disableThumbnailSwipe=False,
        onErrorImageURL=None,
        indexSeparator=' / ',
        slideDuration=450,
        swipingTransitionDuration=0,
        slideInterval=3000,
        slideOnThumbnailOver=True,
        flickThreshold=0.4,
        swipeThreshold=30,
        stopPropagation=False,
        startIndex=0,
        useWindowKeyDown=True,
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True, port='1059')