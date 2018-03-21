//Include Gulp
var gulp = require('gulp');
var connect = require('gulp-connect');
var postcss = require('gulp-postcss');
var pug = require('gulp-pug');
var autoprefixer = require('autoprefixer');
//Define base folders
var static = 'static/';
var dest = 'dest/';
// Include plugins
var plugins = require("gulp-load-plugins")({
  pattern: ['gulp-*', 'gulp.*', 'main-bower-files'],
  replaceString: /\bgulp[\-.]/
});

// Concatenate & Minify JS
gulp.task('scripts', function() {

  var jsFiles = [static + 'js/*'];
  var static = 'static/';
  var dest = '/dest/';
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

  var cssFiles = [static +'css/*'];

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

  return gulp.src('static/styles/*.css',)
    .pipe(postcss([
      tailwindcss('tailwind.js'),
      require('autoprefixer'),
    ]))
    .pipe(gulp.dest('./posts/static/css'))
    .pipe(connect.reload())
});

// This doesn't work. When I change the src link to posts/templates etc,
// it doesnt like the django template tags
gulp.task('html', function() {
  gulp.src('./templates/posts/base.html')
    .pipe(pug())
    .pipe(gulp.dest(dest + 'html'))
});

// Watch for changes in files
// This also doesn't work.
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
gulp.task('default', ['css', 'tailwind', 'html', 'scripts',]);
gulp.task('start', ['connect', 'watch']);
