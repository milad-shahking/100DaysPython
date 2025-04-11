import emoji # type: ignore
from tqdm import tqdm # type: ignore
from time import sleep
print(emoji.emojize("hello world :globe_showing_Americas:"))
print(emoji.emojize('i love you :red_heart:'))

for i in tqdm(range(1000)):
    sleep(0.1)