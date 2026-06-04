import time

sentence = "Python programming is fun and useful."

print("Typing Speed Test")
print("\nType the following sentence:")
print(sentence)

input("\nPress Enter when you are ready...")

start_time = time.time()

typed_text = input("\nStart typing: ")

end_time = time.time()

time_taken = end_time - start_time

words = len(typed_text.split())
wpm = (words / time_taken) * 60

correct_chars = 0
for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(sentence)) * 100

print("\nResults")
print("Time Taken: {:.2f} seconds".format(time_taken))
print("Typing Speed: {:.2f} WPM".format(wpm))
print("Accuracy: {:.2f}%".format(accuracy))
