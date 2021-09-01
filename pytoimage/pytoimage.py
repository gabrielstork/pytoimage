from PIL import Image, ImageDraw, ImageFont


LIMIT = 79
PIXEL = LIMIT * 8
MARGIN = 5


class PyImage:
    def __init__(self, path: str, background: str = '#262626') -> None:
        with open(path, 'r', encoding='utf8') as file:
            self.content = file.readlines()

        self.font = ImageFont.truetype('arial.ttf', 14)

        self.color_pallete = {
            'lines': '#959595',
            'normal': '#FFFFFF',
            'keywords': '#F02727',
        }

        self._lines = len(self.content)
        self._check = Image.new('RGBA', (PIXEL, PIXEL), background)
        self._check_draw = ImageDraw.Draw(self._check)

        self.x, self.y = self._get_max_lines()
        x_size = self._get_max_chars()

        size = (x_size, (self.y * self._lines) + MARGIN)

        self.image = Image.new('RGBA', size, background)
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

        return PIXEL + max(extra)

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
                ((self.x) - x, y * (line - 1) + MARGIN),
                str(line),
                fill=self.color_pallete['lines'],
                font=self.font,
            )

    def _draw_code(self) -> None:
        for n, content in enumerate(self.content):
            self.draw.text(
                ((self.x + MARGIN), (self.y * n) + MARGIN),
                content,
                fill=self.color_pallete['normal'],
                font=self.font,
            )

    def set_font(self, font: str) -> None:
        self.font = ImageFont.truetype(font, 14)

    def set_color_pallete(self, pallete: dict) -> None:
        self.color_pallete.update(pallete)

    def generate_image(self) -> None:
        self._draw_numbers()
        self._draw_code()

    def save_image(self, path: str) -> None:
        self.image.save(path)
