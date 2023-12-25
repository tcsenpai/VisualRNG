# VisualRNG

![API](https://i.imgur.com/nYVBnbD.png)

## What is this

VisualRNG is a small python implementation of some general considerations about randomness.

The goal is, of course, obtain true randomness with a cheap, replicable DIY setup.

## Install and Run

    git clone https://github.com/thecookingsenpai/VisualRNG
    cd VisualRNG
    pip install -r requirements.txt
    python main.py

Once you have done this, you should have a live API on http://localhost:1122.
By visiting the website, you will obtain the random number of that precise frame.

Feel free to change ports and behaviors directly in main.py.

## Is this True Randomness? Is this a True Random Number Generator?

Technically, it could be. The principle is that your randomness is as good as your entropy.
Long story short, entropy is the 'seed' that scrambles the algorithm to produce a random number (sorry cypherpunk friends).

## So what is this?

This is a software that connect to any video capture device (e.g. a webcam) and produce a random number using the actual frame captured by the device.

## More in details?

Let's consider this demo setup:

![Setup](https://i.imgur.com/MRD8W07.png)

On the right, we have that little white RGB bar: this is a small microphone that react to sounds producing a sort of RGB intensity meter.

On the left, we have a common lava lamp bought on Amazon.

The PC I used does not matter, as long as it runs Python 3.8 or higher.

Highlighted due to the small size, we also have the low quality USB camera looking at us.

We assume that at any given moment the sound conditions of the environment are unknown, especially if the microphone is high quality. For the same reason, we assume that the lava lamp melted wax moves in an unpredictable way, creating color strikes and light changes. That said, we also know that by itself a low definition USB camera will produce some unpredictable noise.

See the pattern? We have three strong sources of entropy! But...wouldn't it be complicated to measure all together quickly?

Well, the trick here is that a video frame contains informations taken from the light surrounding the device capturing it. We are directly converting sound into visuals with the microphone RGB bar, while image noise and lava lamp variations are naturally contained in the video frame.

By hashing the image, deriving a number from the hash and using it as a seed for our random number generator, we obtain a high quality random number with a cheap DIY setup.

## Theory summary

Randomness is as good as the goodness of the below entropy. Entropy is good if it is unpredictable, unreplicable and unknown to third parties. Timestamp is often used as entropy source as it has literally a millisecond of life span.

Following this reasoning, any unpredictable entropy source that is only observable by the randomness generator should generate true randomness.

By combining multiple sources of entropy, all highly connected to the local environment and influencing one the other, such as sounds, lights and colors, we obtain a practically unpredictable, unrepicable and highly unstable source of entropy. Combining three different sources also strenghten the resistance of the generator as even the failure of 2 of the 3 sources (e.g. hacked sound card or anything else that breaks up) still offers a reasonable grade of security.

## License

MIT
