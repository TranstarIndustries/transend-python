from .client import TransendAPIClient, BaseAPI, ProductAPI, BranchAPI, VehicleAPI, AccountAPI, ContentAPI, CoreAPI, CustomerAPI

# Make version info available
try:
    import importlib.metadata
    __version__ = importlib.metadata.version("transend")
except (ImportError, importlib.metadata.PackageNotFoundError):
    try:
        # Fallback for Python < 3.8
        import importlib_metadata
        __version__ = importlib_metadata.version("transend")
    except (ImportError, importlib_metadata.PackageNotFoundError):
        __version__ = "unknown"
