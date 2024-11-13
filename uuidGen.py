import uuid

count: int = 0

def generate_uuid() -> str:
	return str(uuid.uuid4())

def main() -> None:
	global count
	count += 1
	print(f' {count}. New UUID: {generate_uuid()}')
	generate_next = input('Generate a new uuid? [y/n]: ') == 'y'
	if generate_next:
		main()

print('\nUUID v4 generator: ')
main()
print(f'\nFinished after generating {count} UUIDs')
