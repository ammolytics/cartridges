# Open Source Cartridge Dataset

A community-maintained dataset of ammunition cartridge information for use by
developers, engineers, data scientists, and anyone who might find it useful.


## Categories

Cartridges have a **lot** of variation, so accuration and maintainable
categorization can be a major obstacle. For the sake of simplicity, we use the
following as top-level categories:

* Handgun
* Rifle
* Rimfire

They aren't perfect, but most cartridges should be immediately recognizable as
one of these. We've gotta start somewhere.


## Boilerplate

**Work In Progress**

The following boilerplate should be used when adding a cartridge to the dataset.
This template may evolve over time and backward-compatibility should be
maintained to the best of our abilities. Language-specific packages based off
of this dataset should use semantic versioning to ensure that format changes
don't break userspace.

```
"<official cartridge name>": {
  "names": [
    "<other names for this cartridge>"
  ],
  "dimensions": {},
  "bullet": {},
  "case": {},
  "standard": "<name of body/org who maintains the spec (e.g.: SAAMI, NATO, CIP, proprietary)>",
  "reference_url": "<url to the source of the information provided here>"
}
```



