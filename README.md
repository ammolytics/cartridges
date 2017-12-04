# Open Source Cartridge Dataset

A community-maintained dataset of ammunition cartridge information for use by developers, engineers, data scientists, and anyone who might find it useful.


## Categories

Cartridges have a **lot** of variation, which presents some challenges for accurate and maintainable categorization. For the sake of simplicity, we use the following as top-level categories:

* Pistol
* Rifle
* Rimfire
* Shotshell

They aren't perfect, but most cartridges should be immediately recognizable as one of these. We've gotta start somewhere.


## Structure

For each category above, there is a section within the top-level `cartridges.json` file listing cartridge names, as well as a directory containing separate JSON files for each cartridge. These separate JSON files will contain relevant information about the cartridge, according to the format below.


## Format

**Work In Progress**

The following template should be used when adding a cartridge to the dataset. This template may evolve over time and backward-compatibility should be maintained to the best of our abilities. Language-specific packages based off of this dataset should use semantic versioning to ensure that format changes don't break userspace.


### Units of measure

Cartridges are often defined in both the Metric and Imperial units of measure. In order to provide maximum flexibility, both units must be provided in the specification file.

```
{
  "name": "<official cartridge name>",
  "names": [
    "<other names for this cartridge>"
  ],
  "diameter_mm": "<bullet diameter in millimeters>",
  "diameter_in": "<bullet diameter in inches>",
  "specs": {
    "coal_mm": "<cartridge overall length in millimeters>",
    "coal_in": "<cartridge overall length in inches>",
    "bullet": {},
    "case": {},
    "primer": {}
  },
  "standard": "<name of body/org who maintains the spec (e.g.: SAAMI, NATO, CIP, proprietary)>",
  "references": [
    "<urls to the sources of the information provided here>"
  ]
}
```


### Filename

The filename should be URL-safe and human readable. Underscores and hyphens are permitted, but the latter should only be used in cases where they exist in the official cartridge name.


# References

* [CIP](http://www.cip-bobp.org/)
* [NATO STANAG](http://standards.globalspec.com/)
* [SAAMI](http://www.saami.org/)
