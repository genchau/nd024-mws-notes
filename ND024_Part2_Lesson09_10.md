# Lesson 9.10 Quiz: Project Part 3

#### Quiz:

Objective:
- Use the picture element to deliver different images based on view port widths.
- For the horse image, create 3 different versions of the images by cropping instead of shrinking.
- Breakpoints can be at 500 and 750. 
- Setup images for 1x and 2x, when viewport is greater than 750px.
- Add alt texts.

My implementation of the project:
[My responsive blog: picture story](https://genchau.github.io/ND024_Part2_Lesson09-10/)
- Used Gulp to auto-generate Large 1x, Large 2x, Medium 1x, Medium 2x, and Small. Then multiply those by 2 to make webp and jpg formats. I had 80 images by then.
- Used Google Drawings and Paint to help make the cropped images.
- Used Google Sheets with string manipulation to help generate line of codes for all the images going into the picture elements.

<details>
<summary>gulpfile.js used to generate the images</summary>
<p>

```
var gulp = require('gulp');
var $ = require('gulp-load-plugins')();

gulp.task('images', function () {
  return gulp.src('images_src/*.jpg')
    .pipe($.responsive({
      '*': [
      {
        width: 2400,
        rename: {
          suffix: '_large_2x_2400w',
          extname: '.jpg',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 1200,
        rename: {
          suffix: '_large_1x_1200w',
          extname: '.jpg',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 1500,
        rename: {
          suffix: '_medium_2x_1500w',
          extname: '.jpg',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 750,
        rename: {
          suffix: '_medium_1x_750w',
          extname: '.jpg',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 500,
        rename: {
          suffix: '_small_500w',
          extname: '.jpg',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 2400,
        rename: {
          suffix: '_large_2x_2400w',
          extname: '.webp',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 1200,
        rename: {
          suffix: '_large_1x_1200w',
          extname: '.webp',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 1500,
        rename: {
          suffix: '_medium_2x_1500w',
          extname: '.webp',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 750,
        rename: {
          suffix: '_medium_1x_750w',
          extname: '.webp',
        },
        withoutEnlargement: true,
      }, 
      {
        width: 500,
        rename: {
          suffix: '_small_500w',
          extname: '.webp',
        },
        withoutEnlargement: true,
      }, 

      ],
    }, {
      // Global configuration for all images
      // The output quality for JPEG, WebP and TIFF output formats
      quality: 40,
      // Use progressive (interlace) scan for JPEG and PNG output
      progressive: true,
      // Strip all metadata
      withMetadata: false,
      // Do not emit the error when image is enlarged.
      errorOnEnlargement: false,
    }))
    .pipe(gulp.dest('img'));
});
```

</p>
</details>

- - -
Next up: [Course Conclusion](ND024_Part2_Lesson09_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
