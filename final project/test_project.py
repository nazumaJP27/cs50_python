import pytest
from project import load_image, load_images, load_images_dict, Game
import pygame
from pygame.surface import Surface


BASE_IMG_PATH = "assets/img/"

# Inicialize pygame in every test
@pytest.fixture
def setup_pygame():
    pygame.init()
    display = pygame.display.set_mode((600, 300))
    yield
    pygame.quit()


def test_load_image(setup_pygame):
    image0 = load_image("player/idle/idle.png")
    image1 = load_image("enemies/zombie/walk/walk0.png")
    image2 = load_image("map/low_collum.png")

    assert isinstance(image0, Surface)
    assert isinstance(image1, Surface)
    assert isinstance(image2, Surface)


def test_load_images(setup_pygame):
    images0 = load_images("player/run")
    images1 = load_images("enemies/zombie/walk")
    images2 = load_images("enemies/ghost/death")

    assert isinstance(images0, list), "returns a list"
    assert all(isinstance(img, Surface) for img in images0)

    assert isinstance(images1, list), "returns a list"
    assert all(isinstance(img, Surface) for img in images1)

    assert isinstance(images2, list), "returns a list"
    assert all(isinstance(img, Surface) for img in images2)


def test_load_images_dict(setup_pygame):
    font0_dict = load_images_dict("fontA")
    font1_dict = load_images_dict("fontB")
    font2_dict = load_images_dict("fontC")
    assert isinstance(font0_dict, dict)
    assert all(isinstance(img, Surface) for img in font0_dict.values())

    assert isinstance(font1_dict, dict)
    assert all(isinstance(img, Surface) for img in font1_dict.values())

    assert isinstance(font2_dict, dict)
    assert all(isinstance(img, Surface) for img in font2_dict.values())


def test_write(setup_pygame): #def write(self, sentence, position, surf, font="fontA", center=False, left=False, symbol=False, scale=1.0, compansate=True): #compansate different widths
    game_class = Game()
    string0 = "hello, world"
    write_info = game_class.write(string0, (100, 50))
    keys_in_dict = write_info[4]

    assert write_info == [100, 50, 100, 192, keys_in_dict]