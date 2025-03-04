#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:


    def get_entity(entity_name, position= (0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}.png', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}.png', (WIN_WIDTH, 0)))
                return list_bg
