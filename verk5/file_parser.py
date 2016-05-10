
def file_parser(file_path):

	smíða dictionary með stagger:
		tag.artist
		tag.title
		tag.album
		tag.track
	SETJA TÓMAN STRENG EF AÐ EITTHVAÐ TAG ER EKKI TIL !



	if artist in dict:
		move_to_artist(file_path, dict)
	else:
		move_to_other(file_path, dict)

