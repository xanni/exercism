#include "queen_attack.h"

#include <stdlib.h>

#define BOARD_SIZE (8)

attack_status_t can_attack(position_t queen_1, position_t queen_2)
{
    if ((queen_1.column == queen_2.column && queen_1.row == queen_2.row) ||
        queen_1.column >= BOARD_SIZE || queen_1.row >= BOARD_SIZE ||
        queen_2.column >= BOARD_SIZE || queen_2.row >= BOARD_SIZE)
        return INVALID_POSITION;

    return (queen_1.column == queen_2.column || queen_1.row == queen_2.row ||
            abs(queen_1.column - queen_2.column) == abs(queen_1.row - queen_2.row))
               ? CAN_ATTACK
               : CAN_NOT_ATTACK;
}
