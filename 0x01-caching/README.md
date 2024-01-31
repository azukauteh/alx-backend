# 0x01. Caching

This directory contains implementations and explanations of various cache replacement policies commonly used in computer science and software engineering. Caching is a fundamental concept in computer science, used to improve data access times by storing frequently accessed data in a faster storage medium.

### Cache Replacement Policies

The directory covers the following cache replacement policies:

1. FIFO (First-In-First-Out):
   - Description: FIFO is a simple cache replacement policy where the oldest item in the cache is evicted first when the cache is full. It operates based on the principle that the item that has been in the cache the longest is the least likely to be needed soon.
   - Implementation: [fifo_cache.py](fifo_cache.py)

2. LIFO (Last-In-First-Out):
   - Description: LIFO is a cache replacement policy where the most recently accessed item is the first to be evicted when the cache is full. It operates based on the principle that the item that has been accessed most recently is the most likely to be needed again soon.
   - Implementation: [lifo_cache.py](lifo_cache.py)

3. LRU (Least Recently Used):
   - Description: LRU is a cache replacement policy where the least recently accessed item is evicted first when the cache is full. It operates based on the principle that the item that has not been accessed for the longest time is the least likely to be needed soon.
   - Implementation: [lru_cache.py](lru_cache.py)

4. MRU (Most Recently Used):
   - Description: MRU is a cache replacement policy where the most recently accessed item is the last to be evicted when the cache is full. It operates based on the principle that the item that has been accessed most recently is the most likely to be needed again soon.
   - Implementation: [mru_cache.py](mru_cache.py)

5. LFU (Least Frequently Used):
   - Description: LFU is a cache replacement policy where the least frequently accessed item is evicted first when the cache is full. It operates based on the principle that the item that has been accessed the fewest number of times is the least likely to be needed soon.
   - Implementation: [lfu_cache.py](lfu_cache.py)

### How to Use

Each cache replacement policy is implemented in a separate Python file. To use a specific cache replacement policy, simply import the corresponding Python file into your project and instantiate the cache object. Detailed usage examples and documentation for each cache replacement policy are provided within their respective Python files.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
