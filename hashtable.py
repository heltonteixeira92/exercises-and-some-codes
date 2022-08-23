class Hashtable:
    def __init__(self, items):
        self.bucket_size = len(items)
        self.buckets = [[i] for i in range(self.bucket_size)]
        self.assign_buckets(items)

    def assign_buckets(self, items):
        for key, value in items:
            has_value = hash(key)
            index = has_value % self.bucket_size
            self.buckets[index].append((key, value))

    def get_value(self, input_keys):
        has_value = hash(input_keys)
        index = has_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_keys:
                return value


