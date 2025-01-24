import chess, os
import random
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
import chess.engine
os.chdir('stockfish')





while True:
    print("""

    _____                            _____ 
    ( ___ )--------------------------( ___ )
    |   |                            |   | 
    |   |   ____ _                   |   | 
    |   |  / ___| |__   ___ ___ ___  |   | 
    |   | | |   | '_ \ / _ / __/ __| |   | 
    |   | | |___| | | |  __\__ \__ \ |   | 
    |   |  \____|_| |_|\___|___|___/ |   | 
    |___|                            |___| 
    (_____)--------------------------(_____)



        CoDeD By Mohammad Taha Gorji
          GitHub: Mr-r0ot




    [ 1 ] Play with keras AI (Easy)
    [ 2 ] Play with EvilCHESS AI (Kids, Medium, Hard, Very Hard, Legend, Demonic, Outside Of Humanity, Incomprehensible, ENDLevel)
    [ 3 ] See Play 2 AI
          
    >> """,end='')
    try:
        s=int(input(""))
    except:
        s=0
    if s==1 or s==2:
        break







if s==1:

    f=['A','B','C','D','E','F','G','H']
    # تابع برای نمایش صفحه شطرنج
    def print_board(board):
        board=(str(board))
        re=""
        n=8
        for e in board.split('''
'''):
            re=(f"""{re}
{n}   {e}""")
            n=(n-1)
        re=(f"""{re}
            
A B C D E F G H""")
        print(re)

    # تابع برای دریافت حرکت کاربر
    def get_user_move(board):
        while True:
            user_input = input("Enter Move: ")
            try:
                move = chess.Move.from_uci(user_input)
                if move in board.legal_moves:
                    return move
                else:
                    print("Invide Move")
            except Exception as e:
                print(f"خطا: {e}. لطفاً دوباره تلاش کنید.")

    # تابع برای ایجاد یک AI ساده
    def simple_ai_move(board):
        return random.choice(list(board.legal_moves))

    # تابع برای تولید دیتا
    def generate_data(board, move):
        # تبدیل صفحه شطرنج به آرایه NumPy
        state = np.zeros((8, 8, 12))  # 12 لایه برای هر نوع مهره
        for piece_type in range(1, 13):
            for square in chess.SQUARES:
                piece = board.piece_at(square)
                if piece and piece.piece_type == piece_type:
                    layer = piece.color * 6 + (piece_type - 1)
                    state[square // 8][square % 8][layer] = 1
        return state.flatten(), move

    # تابع برای ساخت و آموزش مدل
    def build_model():
        model = Sequential()
        model.add(Dense(128, input_shape=(8 * 8 * 12,), activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(4672, activation='softmax'))  # تعداد حرکات قانونی
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    # تابع اصلی
    def main():
        board = chess.Board()
        print_board(board)

        # داده‌ها برای آموزش
        x_data = []
        y_data = []

        model = build_model()

        while not board.is_game_over():
            # نوبت کاربر
            user_move = get_user_move(board)
            x, y = generate_data(board, user_move)
            x_data.append(x)
            y_data.append(y)
            board.push(user_move)
            print_board(board)

            if board.is_game_over():
                break

            # نوبت AI
            print("  AI...")
            ai_move = simple_ai_move(board)
            x, y = generate_data(board, ai_move)
            x_data.append(x)
            y_data.append(y)
            board.push(ai_move)
            print(f"Move AI: {ai_move}")
            print_board(board)

        # تبدیل داده‌ها به آرایه NumPy
        x_data = np.array(x_data)
        y_data = keras.utils.to_categorical(y_data, num_classes=4672)

        # آموزش مدل
        model.fit(x_data, y_data, epochs=10)

        print("End game!")
        print("Return: ", board.result())

    main()







elif s==2:


    # Define difficulty levels
    difficulty_levels = {
        'Kids': {'time':1.0, 'depth': 2},
        'Medium': {'time': 3.0, 'depth': 10},  # 1 second and depth 2
        'Hard': {'time': 4.0, 'depth': 15},  # 2 seconds and depth 4
        'Very Hard': {'time': 7.0, 'depth': 30},  
        'Legend': {'time': 10.0, 'depth': 50},  
        'Demonic': {'time': 13.0, 'depth': 80},  
        'Outside Of Humanity': {'time': 20.0, 'depth': 120},  
        'Incomprehensible': {'time': 30.0, 'depth': 200},  
        'ENDLevel': {'time': 60.0, 'depth': 400}  
    }

    # Function to choose difficulty level
    def choose_difficulty():
        while True:
            e=str(input(" Do you want add level? [(Y)es/(N)o]: ")).lower()
            if 'y' in e:
                t=float(input('Enter Time Ai move(10.0): '))
                d=int(input("Enter depth (Power AI) Ai(5): "))
                return {'time':t, 'depth': d}
            else:
                difficulty = input("Choose (Medium, Hard, Very Hard, Legend, Demonic, Outside Of Humanity, Incomprehensible, ENDLevel): ")
                if difficulty in difficulty_levels:
                    return difficulty
                else:
                    print("Please choose one of the available levels (Medium, Hard, Very Hard, Legend, Demonic, Outside Of Humanity, Incomprehensible, ENDLevel).")

    # Function to display chess board
    def print_board(board):
        board = str(board)
        re = ""
        n = 8
        for e in board.split('\n'):
            re = (f"{re}\n{n}   {e}")
            n = (n - 1)
        re = (f"{re}\n\n    A B C D E F G H")
        print(re)

    # Function to get user's move
    def get_user_move(board):
        while True:
            user_input = input("Enter your move (e.g., e2e4): ")
            try:
                move = chess.Move.from_uci(user_input)
                if move in board.legal_moves:
                    return move
                else:
                    print("Invalid move. Please try again.")
            except Exception as e:
                print(f"Error: {e}. Please try again.")

    # Function to generate AI move using Stockfish
    def advanced_ai_move(board, difficulty):
        # Correct the path to Stockfish executable
        
        stockfish_path = "stockfish-windows-x86-64-avx2.exe"  # Update this path

        try:
            with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
                # Set difficulty level
                time_limit = difficulty_levels[difficulty]['time']
                depth = difficulty_levels[difficulty]['depth']
                
                # Get AI's move with the given time and depth limits
                result = engine.play(board, chess.engine.Limit(time=time_limit, depth=depth))
                return result.move
        except FileNotFoundError:
            print("Error: Stockfish engine not found. Please check the Stockfish path.")
            exit()

    # Function to generate data for training
    def generate_data(board, move):
        state = np.zeros((8, 8, 12))  # 12 layers for each type of piece
        for piece_type in range(1, 13):
            for square in chess.SQUARES:
                piece = board.piece_at(square)
                if piece and piece.piece_type == piece_type:
                    layer = piece.color * 6 + (piece_type - 1)
                    state[square // 8][square % 8][layer] = 1
        return state.flatten(), move

    # Function to build the model
    def build_model():
        model = Sequential()
        model.add(Dense(128, input_shape=(8 * 8 * 12,), activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(4672, activation='softmax'))  # Number of legal moves
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    # Main function
    def main():
        board = chess.Board()
        print_board(board)

        # Choose difficulty level
        difficulty = choose_difficulty()

        # Data for training
        x_data = []
        y_data = []

        model = build_model()

        while not board.is_game_over():
            # User's turn
            user_move = get_user_move(board)
            x, y = generate_data(board, user_move)
            x_data.append(x)
            y_data.append(y)
            board.push(user_move)
            print_board(board)

            if board.is_game_over():
                break

            # AI's turn
            print(f"AI's turn ({difficulty})...")
            ai_move = advanced_ai_move(board, difficulty)
            x, y = generate_data(board, ai_move)
            x_data.append(x)
            y_data.append(y)
            board.push(ai_move)
            print(f"AI move: {ai_move}")
            print_board(board)

        # Convert data to numpy arrays
        x_data = np.array(x_data)
        y_data = keras.utils.to_categorical(y_data, num_classes=4672)

        # Train the model
        model.fit(x_data, y_data, epochs=10)
    
        print("Game over!")
        print("Result:", board.result())

    main()







elif s==3:


    # Function to choose difficulty level
    def choose_difficulty():
        t=float(input('Enter Time Ai move(10.0): '))
        d=int(input("Enter depth (Power AI) Ai(5): "))
        return {'time':t, 'depth': d}

    # Function to display chess board
    def print_board(board):
        board = str(board)
        re = ""
        n = 8
        for e in board.split('\n'):
            re = (f"{re}\n{n}   {e}")
            n = (n - 1)
        re = (f"{re}\n\n    A B C D E F G H")
        print(re)



    # Function to generate AI move using Stockfish
    def advanced_ai_move(board, difficulty):
        # Correct the path to Stockfish executable
        
        stockfish_path = "stockfish-windows-x86-64-avx2.exe"  # Update this path

        try:
            with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
                # Set difficulty level
                time_limit = difficulty_levels[difficulty]['time']
                depth = difficulty_levels[difficulty]['depth']
                
                # Get AI's move with the given time and depth limits
                result = engine.play(board, chess.engine.Limit(time=time_limit, depth=depth))
                return result.move
        except FileNotFoundError:
            print("Error: Stockfish engine not found. Please check the Stockfish path.")
            exit()

    # Function to generate data for training
    def generate_data(board, move):
        state = np.zeros((8, 8, 12))  # 12 layers for each type of piece
        for piece_type in range(1, 13):
            for square in chess.SQUARES:
                piece = board.piece_at(square)
                if piece and piece.piece_type == piece_type:
                    layer = piece.color * 6 + (piece_type - 1)
                    state[square // 8][square % 8][layer] = 1
        return state.flatten(), move

    # Function to build the model
    def build_model():
        model = Sequential()
        model.add(Dense(128, input_shape=(8 * 8 * 12,), activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(4672, activation='softmax'))  # Number of legal moves
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model



    # Main function
    def main():
        board = chess.Board()
        print_board(board)

        # Choose difficulty level
        difficulty = choose_difficulty()

        # Data for training
        x_data = []
        y_data = []

        model = build_model()

        while not board.is_game_over():
            # User's turn
            user_move = get_user_move(board)
            x, y = generate_data(board, user_move)
            x_data.append(x)
            y_data.append(y)
            board.push(user_move)
            print_board(board)

            if board.is_game_over():
                break

            # AI's turn
            print(f"AI's turn ({difficulty})...")
            ai_move = advanced_ai_move(board, difficulty)
            x, y = generate_data(board, ai_move)
            x_data.append(x)
            y_data.append(y)
            board.push(ai_move)
            print(f"AI move: {ai_move}")
            print_board(board)

        # Convert data to numpy arrays
        x_data = np.array(x_data)
        y_data = keras.utils.to_categorical(y_data, num_classes=4672)

        # Train the model
        model.fit(x_data, y_data, epochs=10)
    
        print("Game over!")
        print("Result:", board.result())

    main()


















if s==3:


    

    # Define difficulty levels
    difficulty_levels = {
        'Kids': {'time':1.0, 'depth': 2},
        'Medium': {'time': 3.0, 'depth': 10},  # 1 second and depth 2
        'Hard': {'time': 4.0, 'depth': 15},  # 2 seconds and depth 4
        'Very Hard': {'time': 7.0, 'depth': 30},  
        'Legend': {'time': 10.0, 'depth': 50},  
        'Demonic': {'time': 13.0, 'depth': 80},  
        'Outside Of Humanity': {'time': 20.0, 'depth': 120},  
        'Incomprehensible': {'time': 30.0, 'depth': 200},  
        'ENDLevel': {'time': 60.0, 'depth': 400}  
    }

    # Function to choose difficulty level
    def choose_difficulty():
        while True:
            e=str(input(" Do you want add level? [(Y)es/(N)o]: ")).lower()
            if 'y' in e:
                t=float(input('Enter Time Ai move(10.0): '))
                d=int(input("Enter depth (Power AI) Ai(5): "))
                return {'time':t, 'depth': d}
            else:
                difficulty = input("Choose (Medium, Hard, Very Hard, Legend, Demonic, Outside Of Humanity, Incomprehensible, ENDLevel): ")
                if difficulty in difficulty_levels:
                    return difficulty
                else:
                    print("Please choose one of the available levels (Medium, Hard, Very Hard, Legend, Demonic, Outside Of Humanity, Incomprehensible, ENDLevel).")

    # Function to display chess board
    def print_board(board):
        board = str(board)
        re = ""
        n = 8
        for e in board.split('\n'):
            re = (f"{re}\n{n}   {e}")
            n = (n - 1)
        re = (f"{re}\n\n    A B C D E F G H")
        print(re)

    # Function to generate AI move using Stockfish
    def advanced_ai_move(board, difficulty):
        # Correct the path to Stockfish executable
        
        stockfish_path = "stockfish-windows-x86-64-avx2.exe"  # Update this path

        try:
            with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
                # Set difficulty level
                time_limit = difficulty_levels[difficulty]['time']
                depth = difficulty_levels[difficulty]['depth']
                
                # Get AI's move with the given time and depth limits
                result = engine.play(board, chess.engine.Limit(time=time_limit, depth=depth))
                return result.move
        except FileNotFoundError:
            print("Error: Stockfish engine not found. Please check the Stockfish path.")
            exit()

    # Function to generate data for training
    def generate_data(board, move):
        state = np.zeros((8, 8, 12))  # 12 layers for each type of piece
        for piece_type in range(1, 13):
            for square in chess.SQUARES:
                piece = board.piece_at(square)
                if piece and piece.piece_type == piece_type:
                    layer = piece.color * 6 + (piece_type - 1)
                    state[square // 8][square % 8][layer] = 1
        return state.flatten(), move

    # Function to build the model
    def build_model():
        model = Sequential()
        model.add(Dense(128, input_shape=(8 * 8 * 12,), activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(4672, activation='softmax'))  # Number of legal moves
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    # Main function
    def main():
        board = chess.Board()
        print_board(board)

        # Choose difficulty level
        difficulty = choose_difficulty()

        # Data for training
        x_data = []
        y_data = []

        model = build_model()

        while not board.is_game_over():



            print(f"AI1's turn ({difficulty})...")
            ai1_move = advanced_ai_move(board, difficulty)
            x, y = generate_data(board, ai1_move)
            x_data.append(x)
            y_data.append(y)
            board.push(ai1_move)
            print(f"AI1 move: {ai1_move}")
            print_board(board)
            input('Enter For Next..')

            if board.is_game_over():
                break

            # AI's turn
            print(f"AI2's turn ({difficulty})...")
            ai2_move = advanced_ai_move(board, difficulty)
            x, y = generate_data(board, ai2_move)
            x_data.append(x)
            y_data.append(y)
            board.push(ai2_move)
            print(f"AI2 move: {ai2_move}")
            print_board(board)
            input('Enter For Next..')

        # Convert data to numpy arrays
        x_data = np.array(x_data)
        y_data = keras.utils.to_categorical(y_data, num_classes=4672)

        # Train the model
        model.fit(x_data, y_data, epochs=10)
    
        print("Game over!")
        print("Result:", board.result())

    main()
