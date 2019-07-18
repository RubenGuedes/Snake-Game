from main_imports.all_imports import *

TIME_SLEEP = 0.15

# Desenhar grelha do jogo
def draw_map():
    for x in range(0, MAXSIDE_CANVAS, JUMP):
        x_aux = x + PR_100
        max_w_aux = MAXSIDE_CANVAS + PR_100
        canvas.create_line(x_aux, 0, x_aux, max_w_aux)

    for y in range(0, MAXSIDE_CANVAS, JUMP):
        y_aux = y + PR_100
        max_h_aux = MAXSIDE_CANVAS + PR_100
        canvas.create_line(0, y_aux, max_h_aux, y_aux)

# Verifica se o boneco está dentro dos limites do mapa
def in_limits(pos_x, pos_y):
    return (pos_x >= 0 and pos_x < WIDTH_CANVAS_-JUMP and pos_y >= 0 and pos_y < WIDTH_CANVAS_-JUMP)

# Movimento do boneco
def action(event):
    global game

    # move up
    if event.char == 'w':
        game.dec_y()
    # move down
    elif event.char == 's':
        game.inc_y()
    # move right
    elif event.char == 'd':
        game.inc_x()
    # move left
    elif event.char == 'a':
        game.dec_x()
    else:
        pass


def default_action():
    global game
    atual_dir = game.get_direction()

    if atual_dir == UP:
        game.dec_y()
    # move down
    elif atual_dir == DOWN:
        game.inc_y()
    # move right
    elif atual_dir == RIGHT:
        game.inc_x()
    # move left
    else:
        game.dec_x()

# Termina o jogo
def fim_jogo(root):
    messagebox.showinfo("Game Over","O jogo acabou!")
    root.destroy()

# Movimento da cobra com a Queue
def novo_movimento( x, y, canvas):
    global game

    part = canvas.create_rectangle( x, y, x+JUMP, y+JUMP, fill='green')
    game.add_body_part(part)
    part_rem = game.rem_body_part()
    canvas.delete(part_rem)

def food_map(canvas, game):

    if game.get_food()['o'] == None:
        x = y = -1
        limit = int(WIDTH_CANVAS_-JUMP)
        
        while x == -1 and y == -1:
            x = int(random.randrange(0, limit, JUMP))
            y = int(random.randrange(0, limit, JUMP))

        food = canvas.create_rectangle(x, y, x+JUMP, y+JUMP, fill='orange')
        game.add_food(x, y, food)

def eat(canvas, game, text_label, prev_x, prev_y):
    
    food_x = game.get_food()['x']
    food_y = game.get_food()['y']
    snake_x = game.x()
    snake_y = game.y()

    
    if food_x == snake_x and food_y == snake_y:
        food = game.get_food()['o']
        game.rem_food()

        # Remover comida do campo
        canvas.delete(food)

        # Aumentar o tamanho da cobra
        part = canvas.create_rectangle(prev_x, prev_y, prev_x+JUMP, prev_y+JUMP, fill='green')
        game.add_body_part(part)

        # Aumentar a pontuação
        game.inc_pont()
        text_label.config(text=PONTUATION+"{}".format(game.get_pont()))

#######################################################################
# Configurações Globais
game = Game_conf()
#######################################################################
# Root initial configurations
root = Tk()
root.title(GAME_TITLE)
root.geometry(GEOMETRY_SIZE)
root.minsize(MIN_WIDTH_, MIN_HEIGHT)
root.maxsize(MAX_WIDTH_, MAX_HEIGHT)
#######################################################################
############################# FRAMES ##################################
#######################################################################
# Frame Left (Barra lateral esquerda)
frame_1 = Frame(root, bg=DARKER_BLUE)
frame_1.place(relx=PR_0, rely=PR_0, relwidth=PR_20, relheight=PR_100)

# Frame para o texto (Fica por cima da frame_1 só que não é subframe)
frame_1_1 = Frame(root)
frame_1_1.place(relx=PR_0, rely=PR_0, relwidth=PR_20, relheight=PR_20)

# Frame Right (Espaço para o Mapa)
frame_2 = Frame(root, bg=LIGHTER_BLUE)
frame_2.place(relx=PR_20, rely=PR_0, relwidth=PR_100, relheight=PR_100)
#######################################################################
# Canvas
canvas = Canvas(frame_2, bg=V_BLUE)
canvas.place(relx=PR_5, rely=PR_5, width=WIDTH_CANVAS_, height=WIDTH_CANVAS_)
#######################################################################
# Texto que diz pontuação
text = Label(frame_1_1, text=PONTUATION+"{}".format(game.get_pont()), bg=DARKER_BLUE, font=FONT_20) 
text.place(relx=PR_0, rely=PR_0, relwidth=PR_100, relheight=PR_100)
#######################################################################
# Desenhar o mapa
draw_map()
#######################################################################
# Snake body
part = canvas.create_rectangle(
    game.x(), game.y(), game.x()+JUMP, game.y()+JUMP, fill='green')
game.add_body_part(part)
#######################################################################
# Ciclo responsavel pela acção do boneco
while in_limits(game.x(), game.y()):

    prev_x = copy.copy(game.x())
    prev_y = copy.copy(game.y())

    if prev_x == game.x() and prev_y == game.y():
        default_action()
    
    root.bind('<Key>', action)
    
    root.update()
    sleep(TIME_SLEEP)

    novo_movimento(game.x(), game.y(), canvas)
    food_map(canvas, game)

    eat(canvas, game, text, prev_x, prev_y)

""" Fim do jogo """
fim_jogo(root)

""" Execução do programa """
root.mainloop()
