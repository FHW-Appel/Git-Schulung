import input_reader
import output_writer
import input_handler
import lottery
import output_handler

def main():
    print("🎰 Willkommen bei der Lottoziehung! 🎰")
    
    reader = input_reader.InputReader()  # Standardmäßig von der Konsole lesen
    writer = output_writer.OutputWriter()
    user_numbers = input_handler.get_user_numbers(reader)
    
    drawn_numbers = lottery.draw_lottery_numbers()
    matches, matched_numbers = lottery.check_results(user_numbers, drawn_numbers)
    
    output_handler.print_results(writer, user_numbers, drawn_numbers, matches, matched_numbers)

if __name__ == "__main__":
    main()
