<ImageUpload @file-change="imageFileChangedHandler" />
...
imageFileChangedHandler(b64String) {
  this.image = b64String;
}