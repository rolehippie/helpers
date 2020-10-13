from distutils.version import LooseVersion


class FilterModule(object):
    def filters(self):
        return {
            'version_sort': self.version_sort,
            'version_max': self.version_max,
            'version_min': self.version_min
        }

    def version_sort(self, keys):
        return sorted(keys, key=LooseVersion)

    def version_max(self, keys):
        return sorted(keys, key=LooseVersion)[-1]

    def version_min(self, keys):
        return sorted(keys, key=LooseVersion)[0]
