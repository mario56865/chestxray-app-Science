import sys
import os
import signal


def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()

# this function is modified from the code and knowledge found here: http://supervisord.org/events.html#example-event-listener-implementation


def main():
    while 1:
        write_stdout('READY\n')
        # wait for the event on stdin that supervisord will send
        line = sys.stdin.readline()
        write_stdout('Killing supervisor with this event: ' + line)
        try:
            # supervisord writes its pid to its file from which we read it here, see supervisord.conf
            pidfile = open('/tmp/supervisord.pid', 'r')
            pid = int(pidfile.readline())
            os.kill(pid, signal.SIGQUIT)
        except Exception as e:
            write_stdout('Could not kill supervisor: ' + e.strerror + '\n')
            write_stdout('RESULT 2\nOK')


main()
