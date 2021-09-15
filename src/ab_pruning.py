import math
import sys


def get_possible_moves(tokens, taken_tokens, list_of_taken_tokens, last_move):
    # First move occurring
    if taken_tokens == 0:
        # Floor half of total n tokens
        half = (tokens + 1) // 2
        return [i for i in range(1, half, 2)]

    possible_moves = []

    # Finding factors of the last move
    for x in range(1, int(math.sqrt(last_move)) + 1):
        if (last_move % x == 0) and (x not in list_of_taken_tokens):
            possible_moves.append(x)
            if (last_move // x != x) and (last_move // x not in list_of_taken_tokens):
                print(x)
                possible_moves.append(last_move // x)

    # Finding multiples of the last move
    for y in range(last_move * 2, tokens + 1, last_move):
        if (y not in list_of_taken_tokens) and (y not in possible_moves):
            possible_moves.append(y)

    return possible_moves


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def board_evaluator(taken_tokens, last_move, possible_moves, max_player_turn):
    if len(possible_moves) == 0:
        evaluation_value = -1.0
    elif taken_tokens == 0:
        evaluation_value = 0
    elif last_move == 1:
        if len(possible_moves) % 2 == 0:
            evaluation_value = -0.5
        else:
            evaluation_value = 0.5
    else:
        if is_prime(last_move):
            if len(possible_moves) % 2 == 0:
                evaluation_value = -0.7
            else:
                evaluation_value = 0.7
        else:
            # Largest prime that divides last move
            half = last_move // 2
            counter = 0
            while half:
                if (last_move % half == 0) and (is_prime(half)):
                    # Counting largest prime's multiples
                    for move in possible_moves:
                        if move % half == 0:
                            counter += 1
                    break
            if counter % 2 == 0:
                evaluation_value = -0.6
            else:
                evaluation_value = 0.6
    if max_player_turn:
        return evaluation_value
    return -evaluation_value


def alpha_beta_pruning(tokens, taken_tokens, list_of_taken_tokens, last_move, max_depth, depth, alpha, beta):

    max_player_turn = (taken_tokens % 2 == 0)

    possible_moves = get_possible_moves(tokens, taken_tokens, list_of_taken_tokens, last_move)

    if (len(possible_moves) == 0) or (max_depth != 0 and max_depth == depth):
        return board_evaluator(taken_tokens, last_move, possible_moves, max_player_turn), None

    if max_player_turn:
        value = float(-1000)
        best_move = None

        for move in possible_moves:
            list_of_taken_tokens.append(move)
            value2, move2 = alpha_beta_pruning(tokens, taken_tokens + 1, list_of_taken_tokens, move, max_depth, depth + 1, alpha, beta)
            if (value2 > value) or ((value2 == value) and (best_move is None or move < best_move)):
                value, best_move = value2, move
                alpha = max(alpha, value)

            list_of_taken_tokens.remove(move)

            if value >= beta:
                break

        return value, best_move
    else:
        value = float(1000)
        for move in possible_moves:
            list_of_taken_tokens.append(move)
            value2, move2 = alpha_beta_pruning(tokens, taken_tokens + 1, list_of_taken_tokens, move, max_depth, depth + 1, alpha, beta)
            if (value2 < value) or ((value2 == value) and (best_move is None or move < best_move)):
                value, best_move = value2, move
                beta = min(alpha, value)

            list_of_taken_tokens.remove(move)

            if value <= alpha:
                break

        return value, best_move


def argument_collector():
    tokens_arg = sys.argv[1]
    taken_tokens_arg = sys.argv[2]
    list_of_taken_tokens_arg = []
    for x in range(3, 3 + int(taken_tokens_arg)):
        list_of_taken_tokens_arg.append(int(sys.argv[x]))
    if len(list_of_taken_tokens_arg) > 0:
        last_move_arg = int(list_of_taken_tokens_arg[-1])
    else:
        last_move_arg = None
    max_depth_arg = sys.argv[-1]
    return int(tokens_arg), int(taken_tokens_arg), list_of_taken_tokens_arg, last_move_arg, int(max_depth_arg)


def generate_result_file(output_filename):
    output_path = "../results/"
    output_filename = output_filename + ".txt"
    f = open(output_path + output_filename, "w+")
    f.truncate(0)
    return f


def write_game_given(f, tokens, taken_tokens, list_of_taken_tokens, last_move, max_depth):
    f.write("---Given---")
    f.write("\nTotal number of tokens: " + str(tokens))
    f.write("\nTotal number of taken tokens: " + str(taken_tokens))
    f.write("\nValues of taken tokens: " + str(list_of_taken_tokens))
    f.write("\nLast game move: " + str(last_move))
    f.write("\nMax depth: " + str(max_depth))


def write_game_result(f, value, move):
    f.write("\n---Results---")
    f.write("\nNext computed move: " + str(move))
    f.write("\nStatic board heuristic evaluation: " + str(value))


def main():
    tokens_total, taken_tokens_total, list_taken_tokens, last_move_value, max_depth_search = argument_collector()
    file = generate_result_file("result_" + str(tokens_total) + "_" + str(taken_tokens_total) + "_" + str(max_depth_search))
    write_game_given(file, tokens_total, taken_tokens_total, list_taken_tokens, last_move_value, max_depth_search)
    val, best = alpha_beta_pruning(tokens_total, taken_tokens_total, list_taken_tokens, last_move_value, max_depth_search, 0, float(-1000), float(1000))
    write_game_result(file, val, best)


if __name__ == '__main__':
    main()
