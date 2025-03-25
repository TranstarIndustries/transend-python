# Changelog

All notable changes to the transend-python project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2025-03-24

### Fixed
- Package structure to allow direct import with `from transend import TransendAPIClient`
- Reorganized codebase with proper 'transend' package inside the 'src' directory
- Updated imports in all test files to use the new package structure

[0.1.1]: https://github.com/TranstarIndustries/transend-python/compare/v0.1.0...v0.1.1

## [0.1.0] - 2025-03-21

### Added
- Initial release of the Transend Python API client
- ProductAPI for accessing product information, sorting options, and tags
- BranchAPI for branch details and listings
- VehicleAPI for looking up vehicles by VIN, year/make/model, and accessing vehicle details
- AccountAPI for managing customer accounts, bank accounts, and credit cards
- ContentAPI for retrieving articles and resources
- CoreAPI for accessing core information
- CustomerAPI for retrieving user information
- GitHub Actions workflows for automated testing and PyPI publishing
- Comprehensive test suite using pytest
- Documentation in README.md for installation and usage

[0.1.0]: https://github.com/TranstarIndustries/transend-python/releases/tag/v0.1.0
