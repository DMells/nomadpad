//Include Gulp
var gulp = require('gulp');
var connect = require('gulp-connect');
var postcss = require('gulp-postcss');
var pug = require('gulp-pug');
var autoprefixer = require('autoprefixer');
//Define base folders
var src = 'src/';
var dest = 'posts/static/';
// Include plugins
var plugins = require("gulp-load-plugins")({
  pattern: ['gulp-*', 'gulp.*', 'main-bower-files'],
  replaceString: /\bgulp[\-.]/
});

// Concatenate & Minify JS
gulp.task('scripts', function() {

  var jsFiles = ['src/js/*'];
  //plugins.mainBowerFiles() returns an array of all the main 
  //files from the packages and 
  //plugins.filter('*.js') uses gulp-filter to pass only JS files.
  gulp.src(plugins.mainBowerFiles().concat(jsFiles))
    .pipe(plugins.filter('*.js'))
    .pipe(plugins.concat('main.js'))
    .pipe(plugins.uglify())
    .pipe(gulp.dest(dest + 'js'));

});

// Compile CSS
gulp.task('css', function() {

  var cssFiles = [src +'css/*'];

  gulp.src(plugins.mainBowerFiles().concat(cssFiles))
    .pipe(plugins.filter('*.css'))
    .pipe(plugins.concat('main.css'))
    .pipe(plugins.uglify())
    .pipe(gulp.dest(dest + 'css'));

});

// Compile tailwind

gulp.task('tailwind', function () {
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
    .pipe(gulp.dest(dest + 'html'))
});

// Watch for changes in files
gulp.task('watch', function() {
   gulp.watch(dest + 'css/*.css', ['css']);
   gulp.watch(dest + 'html/*.html', ['html']);
   gulp.watch(dest + 'js/*.js', ['scripts']);

});

gulp.task('connect', function() {
  connect.server({
    root: 'build',
    livereload: true,
    open: true
  });
});

// Default Task
gulp.task('default', ['css', 'tailwind', 'html', 'scripts']);
gulp.task('start', ['connect', 'watch']);
