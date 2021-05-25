CREATE TABLE IF NOT EXISTS `books` (
    book_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(255) NOT NULL,
    book_author VARCHAR(255) NOT NULL,
    book_page_count INT UNSIGNED,
    book_categories VARCHAR(511),
    book_description TEXT,
    book_cover_image_url VARCHAR(511)
)