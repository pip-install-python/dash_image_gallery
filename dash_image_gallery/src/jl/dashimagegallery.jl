# AUTO GENERATED FILE - DO NOT EDIT

export dashimagegallery

"""
    dashimagegallery(;kwargs...)

A DashImageGallery component.

Keyword arguments:
- `id` (String; optional)
- `additionalClass` (String; optional)
- `autoPlay` (Bool; optional)
- `disableKeyDown` (Bool; optional)
- `disableSwipe` (Bool; optional)
- `disableThumbnailScroll` (Bool; optional)
- `disableThumbnailSwipe` (Bool; optional)
- `flickThreshold` (Real; optional)
- `indexSeparator` (String; optional)
- `infinite` (Bool; optional)
- `isRTL` (Bool; optional)
- `items` (required): . items has the following type: Array of lists containing elements 'original', 'thumbnail', 'fullscreen', 'originalHeight', 'originalWidth', 'loading', 'thumbnailHeight', 'thumbnailWidth', 'thumbnailLoading', 'originalClass', 'thumbnailClass', 'renderItem', 'renderThumbInner', 'originalAlt', 'thumbnailAlt', 'originalTitle', 'thumbnailTitle', 'thumbnailLabel', 'description', 'srcSet', 'sizes', 'bulletClass'.
Those elements have the following types:
  - `original` (String; optional)
  - `thumbnail` (String; optional)
  - `fullscreen` (String; optional)
  - `originalHeight` (Real; optional)
  - `originalWidth` (Real; optional)
  - `loading` (String; optional)
  - `thumbnailHeight` (Real; optional)
  - `thumbnailWidth` (Real; optional)
  - `thumbnailLoading` (String; optional)
  - `originalClass` (String; optional)
  - `thumbnailClass` (String; optional)
  - `renderItem` (optional)
  - `renderThumbInner` (optional)
  - `originalAlt` (String; optional)
  - `thumbnailAlt` (String; optional)
  - `originalTitle` (String; optional)
  - `thumbnailTitle` (String; optional)
  - `thumbnailLabel` (String; optional)
  - `description` (String; optional)
  - `srcSet` (String; optional)
  - `sizes` (String; optional)
  - `bulletClass` (String; optional)s
- `lazyLoad` (Bool; optional)
- `onErrorImageURL` (String; optional)
- `showBullets` (Bool; optional)
- `showFullscreenButton` (Bool; optional)
- `showIndex` (Bool; optional)
- `showNav` (Bool; optional)
- `showPlayButton` (Bool; optional)
- `showThumbnails` (Bool; optional)
- `slideDuration` (Real; optional)
- `slideInterval` (Real; optional)
- `slideOnThumbnailOver` (Bool; optional)
- `startIndex` (Real; optional)
- `stopPropagation` (Bool; optional)
- `swipeThreshold` (Real; optional)
- `swipingTransitionDuration` (Real; optional)
- `thumbnailPosition` (String; optional)
- `useBrowserFullscreen` (Bool; optional)
- `useTranslate3D` (Bool; optional)
- `useWindowKeyDown` (Bool; optional)
"""
function dashimagegallery(; kwargs...)
        available_props = Symbol[:id, :additionalClass, :autoPlay, :disableKeyDown, :disableSwipe, :disableThumbnailScroll, :disableThumbnailSwipe, :flickThreshold, :indexSeparator, :infinite, :isRTL, :items, :lazyLoad, :onErrorImageURL, :showBullets, :showFullscreenButton, :showIndex, :showNav, :showPlayButton, :showThumbnails, :slideDuration, :slideInterval, :slideOnThumbnailOver, :startIndex, :stopPropagation, :swipeThreshold, :swipingTransitionDuration, :thumbnailPosition, :useBrowserFullscreen, :useTranslate3D, :useWindowKeyDown]
        wild_props = Symbol[]
        return Component("dashimagegallery", "DashImageGallery", "dash_image_gallery", available_props, wild_props; kwargs...)
end

