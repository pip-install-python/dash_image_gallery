# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashImageGallery(Component):
    """A DashImageGallery component.


Keyword arguments:

- id (string; optional)

- additionalClass (string; optional)

- autoPlay (boolean; default False)

- disableKeyDown (boolean; default False)

- disableSwipe (boolean; default False)

- disableThumbnailScroll (boolean; default False)

- disableThumbnailSwipe (boolean; default False)

- flickThreshold (number; default 0.4)

- indexSeparator (string; default ' / ')

- infinite (boolean; default True)

- isRTL (boolean; default False)

- items (list of dicts; required)

    `items` is a list of dicts with keys:

    - bulletClass (string; optional)

    - description (string; optional)

    - fullscreen (string; optional)

    - loading (string; optional)

    - original (string; optional)

    - originalAlt (string; optional)

    - originalClass (string; optional)

    - originalHeight (number; optional)

    - originalTitle (string; optional)

    - originalWidth (number; optional)

    - renderItem (optional)

    - renderThumbInner (optional)

    - sizes (string; optional)

    - srcSet (string; optional)

    - thumbnail (string; optional)

    - thumbnailAlt (string; optional)

    - thumbnailClass (string; optional)

    - thumbnailHeight (number; optional)

    - thumbnailLabel (string; optional)

    - thumbnailLoading (string; optional)

    - thumbnailTitle (string; optional)

    - thumbnailWidth (number; optional)

- lazyLoad (boolean; default False)

- onErrorImageURL (string; default undefined)

- showBullets (boolean; default False)

- showFullscreenButton (boolean; default True)

- showIndex (boolean; default False)

- showNav (boolean; default True)

- showPlayButton (boolean; default True)

- showThumbnails (boolean; default True)

- slideDuration (number; default 450)

- slideInterval (number; default 3000)

- slideOnThumbnailOver (boolean; default False)

- startIndex (number; default 0)

- stopPropagation (boolean; default False)

- swipeThreshold (number; default 30)

- swipingTransitionDuration (number; default 0)

- thumbnailPosition (string; default 'bottom')

- useBrowserFullscreen (boolean; default True)

- useTranslate3D (boolean; default True)

- useWindowKeyDown (boolean; default True)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_image_gallery'
    _type = 'DashImageGallery'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, items=Component.REQUIRED, infinite=Component.UNDEFINED, lazyLoad=Component.UNDEFINED, showNav=Component.UNDEFINED, showThumbnails=Component.UNDEFINED, thumbnailPosition=Component.UNDEFINED, showFullscreenButton=Component.UNDEFINED, useBrowserFullscreen=Component.UNDEFINED, useTranslate3D=Component.UNDEFINED, showPlayButton=Component.UNDEFINED, isRTL=Component.UNDEFINED, showBullets=Component.UNDEFINED, showIndex=Component.UNDEFINED, autoPlay=Component.UNDEFINED, disableThumbnailScroll=Component.UNDEFINED, disableKeyDown=Component.UNDEFINED, disableSwipe=Component.UNDEFINED, disableThumbnailSwipe=Component.UNDEFINED, onErrorImageURL=Component.UNDEFINED, indexSeparator=Component.UNDEFINED, slideDuration=Component.UNDEFINED, swipingTransitionDuration=Component.UNDEFINED, slideInterval=Component.UNDEFINED, slideOnThumbnailOver=Component.UNDEFINED, flickThreshold=Component.UNDEFINED, swipeThreshold=Component.UNDEFINED, stopPropagation=Component.UNDEFINED, startIndex=Component.UNDEFINED, onImageError=Component.UNDEFINED, onThumbnailError=Component.UNDEFINED, onThumbnailClick=Component.UNDEFINED, onBulletClick=Component.UNDEFINED, onImageLoad=Component.UNDEFINED, onSlide=Component.UNDEFINED, onBeforeSlide=Component.UNDEFINED, onScreenChange=Component.UNDEFINED, onPause=Component.UNDEFINED, onPlay=Component.UNDEFINED, onClick=Component.UNDEFINED, onTouchMove=Component.UNDEFINED, onTouchEnd=Component.UNDEFINED, onTouchStart=Component.UNDEFINED, onMouseOver=Component.UNDEFINED, onMouseLeave=Component.UNDEFINED, additionalClass=Component.UNDEFINED, renderCustomControls=Component.UNDEFINED, renderItem=Component.UNDEFINED, renderThumbInner=Component.UNDEFINED, renderLeftNav=Component.UNDEFINED, renderRightNav=Component.UNDEFINED, renderPlayPauseButton=Component.UNDEFINED, renderFullscreenButton=Component.UNDEFINED, useWindowKeyDown=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'additionalClass', 'autoPlay', 'disableKeyDown', 'disableSwipe', 'disableThumbnailScroll', 'disableThumbnailSwipe', 'flickThreshold', 'indexSeparator', 'infinite', 'isRTL', 'items', 'lazyLoad', 'onErrorImageURL', 'showBullets', 'showFullscreenButton', 'showIndex', 'showNav', 'showPlayButton', 'showThumbnails', 'slideDuration', 'slideInterval', 'slideOnThumbnailOver', 'startIndex', 'stopPropagation', 'swipeThreshold', 'swipingTransitionDuration', 'thumbnailPosition', 'useBrowserFullscreen', 'useTranslate3D', 'useWindowKeyDown']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'additionalClass', 'autoPlay', 'disableKeyDown', 'disableSwipe', 'disableThumbnailScroll', 'disableThumbnailSwipe', 'flickThreshold', 'indexSeparator', 'infinite', 'isRTL', 'items', 'lazyLoad', 'onErrorImageURL', 'showBullets', 'showFullscreenButton', 'showIndex', 'showNav', 'showPlayButton', 'showThumbnails', 'slideDuration', 'slideInterval', 'slideOnThumbnailOver', 'startIndex', 'stopPropagation', 'swipeThreshold', 'swipingTransitionDuration', 'thumbnailPosition', 'useBrowserFullscreen', 'useTranslate3D', 'useWindowKeyDown']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['items']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashImageGallery, self).__init__(**args)
