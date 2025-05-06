# GPX to PNG converter service
This service can be used to convert GPX files to PNG using the original 
gpx2png.pl script.

The perl script uses openstreetmap to get the map tiles.

Don't blame me for anything. I just needed this to generate images from
GPX files for a cycling club I'm connected to ;)

**This repository is unmaintained and has been archived as of 2025-05-06**

## Starting it up.
Copy docker-compose.dist.yml to docker-compose.yml. Adjust the file
to your own needs and run:

```bash
docker-compose up -d
```

This will build the docker image and listen on port 5000 by default.

## Example usage
Example with curl:

```bash
curl -XPOST --data-binary @yourawesomeroute.gpx http://localhost:5000 > awesomeness.png
```

Just post the raw .gpx file to the service and the png data will be returned.
