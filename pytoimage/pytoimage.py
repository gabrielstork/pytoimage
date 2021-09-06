from PIL import Image, ImageDraw, ImageFont

LIMIT = 79
WIDTH = 600
MARGIN = 5


class PyImage:
    def __init__(self, path: str, background: str = '#0D1117') -> None:
        with open(path, 'r', encoding='utf8') as file:
            self.content = file.readlines()

        self.font = ImageFont.truetype(
            'fonts/Inconsolata_SemiCondensed-ExtraBold.ttf',
            16,
        )

        self.color_pallete = {
            'line': '#959595',
            'normal': '#FFFFFF',
        }

        self._lines = len(self.content)
        self._check = Image.new('RGB', (WIDTH, WIDTH), background)
        self._check_draw = ImageDraw.Draw(self._check)

        self.x_line, self.y_line = self._get_max_lines()
        self.x = self._get_max_chars()
        self.y = (self.y_line * self._lines) + MARGIN

        self.image = Image.new('RGB', (self.x, self.y), background)
        self.draw = ImageDraw.Draw(self.image)

    def _get_max_chars(self) -> int:
        extra = [0]

        for content in self.content:
            if len(content) > LIMIT:
                x_max, _ = self._check_draw.textsize(
                    content[LIMIT:],
                    font=self.font,
                )

                extra.append(x_max)

        return WIDTH + max(extra)

    def _get_max_lines(self) -> tuple:
        x_max, y_max = self._check_draw.textsize(
            f'0{str(self._lines)}',
            font=self.font,
        )

        return (x_max, y_max + MARGIN)

    def _draw_numbers(self) -> None:
        for line in range(1, self._lines + 1):
            x, y = self.draw.textsize(
                str(line),
                font=self.font,
            )

            x += MARGIN
            y += MARGIN

            self.draw.text(
                ((self.x_line) - x, y * (line - 1) + MARGIN),
                str(line),
                fill=self.color_pallete['line'],
                font=self.font,
            )

    def _draw_code(self) -> None:
        for n, content in enumerate(self.content):
            self.draw.text(
                ((self.x_line + MARGIN), (self.y_line * n) + MARGIN),
                content,
                fill=self.color_pallete['normal'],
                font=self.font,
            )

    def set_font(self, path: str) -> None:
        self.font = ImageFont.truetype(path, 16)

    def set_color_pallete(self, pallete: dict) -> None:
        self.color_pallete.update(pallete)

    def generate_image(self, start: int = 0, end: int = 0) -> None:
        self._draw_numbers()
        self._draw_code()

        top = 0
        bottom = self.y

        if start > 0:
            top = ((start - 1) * self.y_line) + MARGIN
        if end > 0:
            if end > self._lines:
                end = self._lines
            bottom = self.y - ((self._lines - end) * self.y_line)

        self.image = self.image.crop((0, top, self.x, bottom))

    def show_image(self) -> None:
        self.image.show()

    def save_image(self, path: str) -> None:
        self.image.save(path)
