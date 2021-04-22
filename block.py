class Block:
        def __init__(self, previous_block_hash, data, timestamp):
            self.previous_block_hash = previous_block_hash
            self.data = data
            self.timestamp = timestamp
            self.hash self.get_hash
        
        def get_hash(self):
            header_bin = (str(self.previous_block_hash)+
                        str(self.data)+
                        str(self.timestamp)).encode()
            
            