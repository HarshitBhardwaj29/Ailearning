from ai_service import summarize, translate, sentiment
import argparse

parser = argparse.ArgumentParser(
    description="AI Toolkit CLI"
)

parser.add_argument(
    "action",
    choices=["summarize", "translate", "sentiment"]
)

parser.add_argument("text")

parser.add_argument(
    "--language",
    default="Hindi"
)

args = parser.parse_args()

if args.action == "summarize":
    print(summarize(args.text))

elif args.action == "sentiment":
    print(sentiment(args.text))

elif args.action == "translate":
    print(translate(args.text, args.language))