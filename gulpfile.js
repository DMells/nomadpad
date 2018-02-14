var gulp = require('gulp');
var postcss = require('gulp-postcss');
var pug = require('gulp-pug');
var autoprefixer = require('autoprefixer');
var connect = require('gulp-connect');

gulp.task('css', function () {
  var postcss = require('gulp-postcss');
  var tailwindcss = require('tailwindcss');

  return gulp.src('./src/styles.css')
    .pipe(postcss([
      tailwindcss('./tailwind.js'),
      require('autoprefixer'),
    ]))
    .pipe(gulp.dest('./posts/static/css'))
    .pipe(connect.reload())
});

gulp.task('html', function() {
  gulp.src('./templates/posts/base.html')
    .pipe(pug())
    .pipe(gulp.dest('./posts/static/html'))
});

gulp.task('watch', function() {
   gulp.watch('./posts/static/css/styles.css', ['css']);
   gulp.watch('./posts/static/html/base.html', ['html']);

});

gulp.task('connect', function() {
  connect.server({
    root: 'build',
    livereload: true,
    open: true
  });
});
gulp.task('default', ['css', 'html']);
gulp.task('start', ['connect', 'watch']);