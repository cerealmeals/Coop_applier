import argparse
import add_file
import driver


def resume(args):
    add_file.add_resume(args.path, args.priority, args.keyword)
    return

def cover_letter(args):
    add_file.add_cover_letter(args.path, args.priority, args.keyword)
    return

def applier(args):
    driver.main(args.user, args.password, args.search)
    return

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_resume = subparsers.add_parser('resume', help='argument for adding resumes their keywords and priorities')
parser_resume.add_argument('path', type=str, help='The path the the resume you want to add')
parser_resume.add_argument('keyword', type=str, help='The keyword to search the jopb title with, case insensitive')
parser_resume.add_argument('priority', type=int, help='The priority of the resume in the keyword search')
parser_resume.set_defaults(func=resume)

parser_cover = subparsers.add_parser('cover', help='argument for adding cover letters their keywords and priorities')
parser_cover.add_argument('path', type=str, help='The path the the resume you want to add')
parser_cover.add_argument('keyword', type=str, help='The keyword to search the jopb title with, case insensitive')
parser_cover.add_argument('priority', type=int, help='The priority of the resume in the keyword search')
parser_cover.set_defaults(func=cover_letter)

parser_applier = subparsers.add_parser('applier', help='argument for appling to jobs')
parser_applier.add_argument('user', type=str, help='Your username (computing ID) to login to SFU, case sensitive')
parser_applier.add_argument('password', type=str, help='Your password to loging to SFU, case sensitive')
parser_applier.add_argument('search', type=str, help='The name of the custom saved search saved on the Coop board')
parser_applier.set_defaults(func=applier)

args = parser.parse_args()
args.func(args)

