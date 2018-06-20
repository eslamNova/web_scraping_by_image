## Image-based web scraping software

This software system will be web scraper that uses image to search web sites, it will be designed to minimize the time taken to collect information about product category in an online e-commerce platform, it will only need a picture or text of that product (ex: mobile picture), And it will provide an easy to read report that contain links ,prices and names of that product from a list of online market websites, this report can be tremendously useful in market evaluation witch is an important part of visibility study,  it also can be use full for searching and facilitating purchase from most of online e-commerce platforms.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Window 10

Python 3.6

You need to have [tensorflow](https://www.tensorflow.org/install/install_windows) and [selenium]( http://selenium-python.readthedocs.io/installation.html) libraries installed on your machine

We recommend using [sublime-text]( https://www.sublimetext.com/) for editing code

### Installing

First, clone or download ZIP the software

```
clone https://github.com/eslamNova/web_scraping_by_image.git
```

Open Scraper.py from *web_scraping_by_image\web_scraping* and edit your paths as following

Line 20 – Chrome driver path

```
path ='YOUR PATH/chromedriver_win32/chromedriver.exe'
```

Line 21 – Output folder for storing CSV results

```
save_path = 'YOUR PATH/web_scraping_by_image/output'
```


Save and close Scraper.py

Move to gui.py from *web_scraping_by_image\object_detection*


Line 14 – edit path to web_scraping folder

```
sys.path.append("YOUR PATH/web_scraping_by_image/web_scraping")
```

You are done, the software now should be working.. scrap the web

Open CMD from object_detection folder and run 

```
Py gui.py
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Islam Ashraf** - *Initial work* - [eslamNova]( https://github.com/eslamNova)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


