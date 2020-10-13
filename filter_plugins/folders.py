class FilterModule(object):
    def filters(self):
        return {
            'unique_folders': self.unique_folders
        }

    def unique_folders(self, keys):
        paths = set()
        for key in keys:
            if "/" in key:
                paths.add(key.split("/")[0])

        return list(paths)
