from collections import defaultdict, Counter

n = int(input("Enter the number of messages: "))
chat = defaultdict(list)
all_messages = []

# Input messages
for i in range(n):
    name, message = input().split(':', 1)
    name, message = name.strip(), message.strip()
    chat[name].append((i, message))
    all_messages.append((i, name, message))

# Helper Functions
def total_messages():
    return sum(len(msgs) for msgs in chat.values())

def total_words():
    return sum(len(msg.split()) for _, _, msg in all_messages)

def average_words():
    total = total_words()
    count = total_messages()
    return round(total / count, 2) if count else 0

def longest_message():
    longest = max(all_messages, key=lambda x: len(x[2]), default=None)
    return f"{longest[1]}: {longest[2]}" if longest else "No messages"

def most_active_user():
    return max(chat.items(), key=lambda x: len(x[1]), default=(None, []))

def user_message_count(user):
    return len(chat.get(user, []))

def most_frequent_word(user):
    words = []
    for _, msg in chat.get(user, []):
        words.extend(msg.lower().split())
    if not words:
        return "No messages"
    counter = Counter(words)
    return counter.most_common(1)[0][0]

def user_first_last(user):
    msgs = chat.get(user)
    if not msgs:
        return None
    return f"{user}: {msgs[0][1]}", f"{user}: {msgs[-1][1]}"

def common_repeated_words():
    words = []
    for _, _, msg in all_messages:
        words.extend(msg.lower().split())
    return {word for word, count in Counter(words).items() if count > 1}

def longest_avg_user():
    max_avg, user_name = 0, None
    for user, msgs in chat.items():
        total_words = sum(len(msg.split()) for _, msg in msgs)
        avg = total_words / len(msgs) if msgs else 0
        if avg > max_avg:
            max_avg, user_name = avg, user
    return user_name, round(max_avg, 2)

def mention_count(target):
    return sum(1 for _, _, msg in all_messages if target.lower() in msg.lower())

def remove_duplicates():
    seen = set()
    unique = []
    for _, user, msg in all_messages:
        if (user, msg) not in seen:
            seen.add((user, msg))
            unique.append(f"{user}: {msg}")
    return unique

def sort_messages():
    return sorted([f"{user}: {msg}" for _, user, msg in all_messages])

def extract_questions():
    return [f"{user}: {msg}" for _, user, msg in all_messages if '?' in msg]

def reply_ratio(user1, user2):
    u1_msgs = [i for i, u, _ in all_messages if u == user1]
    replies = 0
    for i, u, msg in all_messages:
        if u == user2 and any(str(j) in msg or user1 in msg for j in u1_msgs):
            replies += 1
    return replies

def deleted_messages():
    return [f"{user}: {msg}" for _, user, msg in all_messages if msg.strip().lower() == "this message was deleted"]

# Menu
while True:
    print("\nMenu:")
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("13. Identify the user with the longest average message length")
    print("14. Count how many messages mention a specific user")
    print("15. Remove duplicate messages")
    print("16. Sort messages alphabetically")
    print("17. Extract all questions asked in the chat")
    print("18. Calculate the reply ratio between two users")
    print("19. Check for deleted messages")
    print("0. Exit")

    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        print(f"Total number of messages: {total_messages()}")

    elif ch == 2:
        print(f"Unique users: {list(chat.keys())}")

    elif ch == 3:
        print(f"Total words in chat: {total_words()}")

    elif ch == 4:
        print(f"Average words per message: {average_words()}")

    elif ch == 5:
        print(f"Longest message: \"{longest_message()}\"")

    elif ch == 6:
        user, msgs = most_active_user()
        print(f"Most active user: {user} ({len(msgs)} messages)")

    elif ch == 7:
        u = input("Enter user name: ")
        print(f"Messages sent by {u}: {user_message_count(u)}")

    elif ch == 8:
        u = input("Enter user name: ")
        print(f"Most frequent word used by {u}: \"{most_frequent_word(u)}\"")

    elif ch == 9:
        u = input("Enter user name: ")
        fl = user_first_last(u)
        if fl:
            print(f"First message by {u}: \"{fl[0]}\"")
            print(f"Last message by {u}: \"{fl[1]}\"")
        else:
            print(f"No messages found for user {u}.")

    elif ch == 10:
        u = input("Enter user name: ")
        if u in chat:
            print(f"User '{u}' found in the chat.")
        else:
            print(f"User '{u}' not found in the chat.")

    elif ch == 11:
        print(f"Common repeated words: {common_repeated_words()}")

    elif ch == 13:
        u, avg = longest_avg_user()
        print(f"User with longest average message: {u} (avg {avg} words)")

    elif ch == 14:
        u = input("Enter user to search mentions: ")
        print(f"Messages mentioning '{u}': {mention_count(u)}")

    elif ch == 15:
        unique_msgs = remove_duplicates()
        print(f"Unique messages count: {len(unique_msgs)}")
        for msg in unique_msgs:
            print(msg)

    elif ch == 16:
        print("Sorted messages A-Z:")
        for msg in sort_messages():
            print(msg)

    elif ch == 17:
        print("Questions in chat:")
        for q in extract_questions():
            print(q)

    elif ch == 18:
        u1 = input("Enter first user: ")
        u2 = input("Enter second user: ")
        print(f"Reply ratio from {u2} to {u1}: {reply_ratio(u1, u2)} replies")

    elif ch == 19:
        d = deleted_messages()
        print(f"Deleted messages found: {len(d)}")
        for msg in d:
            print(msg)

    elif ch == 0:
        print("Exiting...")
        break

    else:
        print("Invalid input")
