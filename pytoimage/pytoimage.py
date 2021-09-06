from PIL import Image, ImageDraw, ImageFont

LIMIT = 79
WIDTH = 600
MARGIN = 5
BACKGROUND = (15, 15, 15)
FONT = 'fonts/Inconsolata.ttf'


class PyImage:
    def __init__(
        self,
        path: str,
        background: tuple = BACKGROUND,
        font: str = FONT,
    ) -> None:

        with open(path, 'r', encoding='utf8') as file:
            self.content = file.readlines()

        self.font = ImageFont.truetype(font, 16)

        self.color_palette = {
            'line': (149, 149, 149),
            'normal': (255, 255, 255),
        }

        self._lines = len(self.content)
        self._check = Image.new('RGB', (WIDTH, WIDTH), background)
        self._check_draw = ImageDraw.Draw(self._check)

        self._x_lines, self._y_lines = self._get_max_lines()
        self.x = self._get_max_chars()
        self.y = (self._y_lines * self._lines) + MARGIN

        self.image = Image.new('RGB', (self.x, self.y), background)
        self._draw = ImageDraw.Draw(self.image)

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
            x, y = self._draw.textsize(
                str(line),
                font=self.font,
            )

            x += MARGIN
            y += MARGIN

            self._draw.text(
                ((self._x_lines) - x, y * (line - 1) + MARGIN),
                str(line),
                fill=self.color_palette['line'],
                font=self.font,
            )

    def _draw_code(self) -> None:
        for n, content in enumerate(self.content):
            self._draw.text(
                ((self._x_lines + MARGIN), (self._y_lines * n) + MARGIN),
                content,
                fill=self.color_palette['normal'],
                font=self.font,
            )

    def set_color_palette(self, palette: dict) -> None:
        self.color_palette.update(palette)

    def generate_image(self, start: int = 0, end: int = 0) -> None:
        self._draw_numbers()
        self._draw_code()

        top = 0
        bottom = self.y

        if start > 0:
            top = ((start - 1) * self._y_lines) + MARGIN
        if end > 0:
            if end > self._lines:
                end = self._lines
            bottom = self.y - ((self._lines - end) * self._y_lines)

        self.image = self.image.crop((0, top, self.x, bottom))

    def show_image(self) -> None:
        self.image.show()

    def save_image(self, path: str) -> None:
        self.image.save(path)
